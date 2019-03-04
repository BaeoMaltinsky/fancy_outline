import re
from markdown.util import etree
from markdown import Extension
from markdown.treeprocessors import Treeprocessor


__version__ = "1.3.0"


class OutlineProcessor(Treeprocessor):
    def process_nodes(self, node):
        s = []
        pattern = re.compile('^h(\d)')
        wrapper_cls = self.wrapper_cls

        for child in node.getchildren():
            match = pattern.match(child.tag.lower())

            if match:
                depth = int(match.group(1))

                section = etree.SubElement(node, self.wrapper_tag)
                section.append(child)

                if self.move_attrib:
                    for key, value in list(child.attrib.items()):
                        section.set(key, value)
                        del child.attrib[key]

                node.remove(child)

                if '%(LEVEL)d' in self.wrapper_cls:
                    wrapper_cls = self.wrapper_cls % {'LEVEL': depth}

                cls = section.attrib.get('class')
                if cls:
                    section.attrib['class'] = " ".join([cls, wrapper_cls])
                elif wrapper_cls:  # no class attribute if wrapper_cls==''
                    section.attrib['class'] = wrapper_cls

                contained = False

                while s:
                    container, container_depth = s[-1]
                    if depth <= container_depth:
                        s.pop()
                    else:
                        contained = True
                        break

                if contained:
                    container.append(section)
                    node.remove(section)

                s.append((section, depth))

            else:
                if s:
                    container, container_depth = s[-1]
                    container.append(child)
                    node.remove(child)

    def jump(self, root):
        """Adds jump to top link at end of section with specified depth"""
        # check for <JTT/> in markdown
        jtt = root.find(".//JTT")
        if jtt is None:
            return
        else:
            level = jtt.get("level")
            link_text = jtt.get("text")
        # defaults until I figure out how markdown extension configs work
        if link_text is None:
            link_text = "Jump to Top"
        if level is None:
            level = "1"

        # get all elements with tag section and class='section%s' level
        elements = root.findall(".//section[@class='section%s']" % level)
        for e in elements:
            jumper = etree.SubElement(e, "a", attrib={"class": "jump-to-top",
                                                      "href": "#"})
            jumper.text = link_text

    def run(self, root):
        self.wrapper_tag = self.config.get('wrapper_tag')[0]
        self.wrapper_cls = self.config.get('wrapper_cls')[0]
        self.move_attrib = self.config.get('move_attrib')[0]
        self.process_nodes(root)
        self.jump(root)
        return root


class OutlineExtension(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'wrapper_tag': ['section', 'Tag name to use, default: section'],
            'wrapper_cls': ['section%(LEVEL)d', 'Default CSS class applied to sections'],
            'move_attrib': [True, 'Move header attributes to the wrapper']
        }
        super(OutlineExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        ext = OutlineProcessor(md)
        ext.config = self.config
        md.treeprocessors.add('outline', ext, '_end')


def makeExtension(configs={}):
    return OutlineExtension(configs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

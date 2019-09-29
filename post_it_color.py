import yaml

class PostItColor(yaml.YAMLObject):
    """Class representing post-it color information (type of post-it, real color (RGB), detected color)"""
    yaml_tag = u"!PostIt"

    def __init__(self, color, type, rgb):
        """Constructor of the class with detected color (based on the config file), 
        type and real RGB color of the post-it as parameters"""
        self.color = color
        self.type = type
        self.rgb = rgb

    def __repr__(self):
        """Representation of the post-it"""
        string = "Post-it {1} [{0}] (RGB = {2})".format(self.type, self.color, self.rgb)
        return string

    def __str__(self):
        """Called function when we want to display the data of the post-it with the 'print' function"""
        return repr(self)

    @staticmethod
    def from_yaml(loader, node):
        """Convert the input YAML flow in an instance of PostIt"""
        nodeMap = loader.construct_mapping(node)
        return PostItColor(color  = nodeMap['color'],
                    type = nodeMap['type'],
                    rgb = nodeMap['rgb'])
    
yaml.add_constructor(PostItColor.yaml_tag, PostItColor.from_yaml, Loader=yaml.SafeLoader)

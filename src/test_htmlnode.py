import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    # Test de l'initialisation avec des valeurs par défaut
    def test_initialization_default(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    # Test de l'initialisation avec des valeurs spécifiques
    def test_initialization_with_values(self):
        node = HTMLNode("div", "Hello", ["child1", "child2"], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, ["child1", "child2"])
        self.assertEqual(node.props, {"class": "container"})

    # Test de la méthode __repr__
    def test_repr(self):
        node = HTMLNode("div", "Hello", None, {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(div, Hello, None, {'class': 'container'})")

    # Test de la méthode props_to_html()
    def test_props_to_html(self):
        node = HTMLNode("div", "Hello", None, {"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')

    # Test pour gérer les props None
    def test_props_to_html_with_no_props(self):
        node = HTMLNode("div", "Hello", None, None)
        self.assertEqual(node.props_to_html(), "")

    # Test pour s'assurer que la méthode to_html soulève une exception
    def test_to_html_raises_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

class TestLeafNode(unittest.TestCase):

    # Test de l'initialisation avec des valeurs par défaut
    def test_initialization_default(self):
        node = LeafNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.props)

    # Test de l'initialisation avec des valeurs spécifiques
    def test_initialization_with_values(self):
        node = LeafNode("span", "Text", {"class": "highlight"})
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Text")
        self.assertEqual(node.props, {"class": "highlight"})

    # Test de la méthode to_html() avec une balise et une valeur
    def test_to_html_with_tag_and_value(self):
        node = LeafNode("span", "Text", {"class": "highlight"})
        expected_html = '<span class="highlight">Text</span>'
        self.assertEqual(node.to_html(), expected_html)

    # Test de la méthode to_html() sans balise (juste la valeur)
    def test_to_html_without_tag(self):
        node = LeafNode(value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    # Test de la méthode to_html() pour s'assurer qu'une exception est levée si value est None
    def test_to_html_raises_value_error_if_value_is_none(self):
        node = LeafNode(tag="span", props={"class": "highlight"})
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()

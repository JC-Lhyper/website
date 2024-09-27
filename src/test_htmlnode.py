import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()

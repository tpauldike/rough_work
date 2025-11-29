# Learning `HTML`
HTML stands for HyperText Markup Language. It's the code that defines the structure and content of a webpage.
HTML is made up of elements, such as; *headings (h1-h6), paragraph (p)*. Most elements have an opening tag and a closing tag, that are conventionally written in lowercase letters. There are void elements that do not have closing tags (e.g; `<img>`) which may have the unnecessary backward slash added (i.e; `<img />`).

An attribute is a special value used to adjust the behavior for an HTML element. It is placed inside the opening tag of an HTML element; an example is `src` and `alt` for `img`. The basic syntax of attributes is `<element attribute="value"></element>`. There are also boolean attributes, such as; *readonly, required, checked, disabled*.
The `link` element is used to link to external resources like *stylesheets* and *site icons*. Here is the basic syntax for using the link element for an external CSS file:

`<link rel="stylesheet" href="./styles.css" />`

The `rel` attribute defines the relationship between the resource that’s being linked and the HTML document (such as; *stylesheet, preconnect, icon*), while the `href` attribute specifies the location of the linked file or resource.
**HTML boiler plate** is simply the ready–made template that defines the basic structure of the document, and this is what it looks like:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
       name="viewport"
       content="width=device-width, initial-scale=1.0" />
    <title>Topman Paul-Dike</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
	<main>
	</main>
	<footer>
	</footer>
  </body>
</html>
```
Character encoding is the method computers use to store characters as data and *UTF–8 (Unicode Transformation Format – 8-bit)* is the most widely used one. *UCS* stands for *Universal Character Set*. It’s the core character set defined by *Unicode and ISO/IEC 10646*, covering virtually all characters used in writing systems worldwide.

Commenting allows you to leave messages without affecting the browser display. It also allows you to make code inactive. A comment in HTML starts with `<!--, contains any number of lines of text, and ends with -->`.

The entire contents of the page are nested within an `html` element. The `html` element is the root element of an HTML page and wraps all content on the page. The `head` element is used to contain metadata about the document, such as its `title`, links to stylesheets, and scripts.
Metadata is information about the page that isn't displayed directly on the page; all page content elements that should be rendered to the page go inside the `body` element. The  `main`  element is used to represent the main content of the body of an HTML document. Content inside the  `main`  element should be unique to the document and should not be repeated in other parts of the document.
The `section` element is used to define sections in a document, such as *chapters, headers, footers*, or any other sections of the document. It is a semantic element that helps with SEO and accessibility. The anchor tag is used to turn a text or other elements to a clinkable link, the `href` attribute specifies the link while the target attribute determines where the link opens.
The `figure` element represents self-contained content and will allow you to associate an *image* with a *caption*. You use it by nesting the `img` element in it alongside the `figcaption` element that contains the title of the image. `em` is used to place emphasis on a specific word or group of words; The `strong` element is used to indicate that some text is of strong importance or urgent.
`<ul>` is used for making unordered lists while `<ol>` is used to create ordered lists; the former displays with bulletins while the later displays numbered lists in order, and `<li>` elements are nested in them to add each member of the list.
The `footer`  element is used to define a footer for a document or section. A footer typically contains information about the author of the document, copyright data, links to terms of use, contact information, and more
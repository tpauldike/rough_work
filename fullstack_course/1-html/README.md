# Learning `HTML`
The purpose of this README is to remind myself of the things I learned; although, someone can read and learn but `HTML` is not something you learn by reading, you rather learn it by doing. I learned these things with practical exercises that might be cumbersome to share here in such a way that a newbie can learn it all. So, if you want to learn directly from me, simply [send me an email](mailto:topman4loveworld@gmail.com)
## Introduction
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

Commenting allows you to leave messages without affecting the browser display. It also allows you to make code inactive. A comment in HTML starts with `<!--`, contains any number of lines of text, and ends with `-->`.

The entire contents of the page are nested within an `html` element. The `html` element is the root element of an HTML page and wraps all content on the page. The `head` element is used to contain metadata about the document, such as its `title`, links to stylesheets, and scripts.
Metadata is information about the page that isn't displayed directly on the page; all page content elements that should be rendered to the page go inside the `body` element. The  `main`  element is used to represent the main content of the body of an HTML document. Content inside the  `main`  element should be unique to the document and should not be repeated in other parts of the document.
The `section` element is used to define sections in a document, such as *chapters, headers, footers*, or any other sections of the document. It is a semantic element that helps with SEO and accessibility. The anchor tag is used to turn a text or other elements to a clinkable link, the `href` attribute specifies the link while the target attribute determines where the link opens.
The `figure` element represents self-contained content and will allow you to associate an *image* with a *caption*. You use it by nesting the `img` element in it alongside the `figcaption` element that contains the title of the image. `em` is used to place emphasis on a specific word or group of words; The `strong` element is used to indicate that some text is of strong importance or urgent.
`<ul>` is used for making unordered lists while `<ol>` is used to create ordered lists; the former displays with bulletins while the later displays numbered lists in order, and `<li>` elements are nested in them to add each member of the list.
The `footer`  element is used to define a footer for a document or section. A footer typically contains information about the author of the document, copyright data, links to terms of use, contact information, and more.

## `div`, IDs, Classes, Entities and Scripts in HTML
The `div` element is used as a container, mainly when you want to group HTML elements that will share a set of CSS styles. Even though the `div` element is commonly used in real world codebases, you should be careful not to overuse it. There are times when another element would be more appropriate. For example, if you wanted to divide up your content into sections, then the `section` element would be more appropriate than a `div` element. The `section` element has semantic meaning over the `div` element which is not semantic.

The *id* attribute adds a unique identifier to an HTML element. *id* names should not be used more than once, and they should always be unique; also, they cannot have spaces in them, unlike the class attribute value that does not need to be unique and can contain spaces to assign multiple classes to a `div`. *Classes* are best used when you want to apply a set of styles to many elements. If you want to target a specific element, it is best to use *id*.

An HTML entity, or character reference, is a set of characters used to represent a reserved character in HTML; it makes it possible for the character that would be interpreted by the browser as special or part of HTML syntax to be displayed as an ordinary text. So, certain characters are typed in the editor to refer to the reserved character, in order to not confuse the browser.
In other words, HTML entities are special codes used to display characters that:
- Are reserved in HTML (e.g., <, >, &)
- Cannot be typed directly from the keyboard (e.g., © ® € →)
- Could break your markup or cause ambiguity

They ensure your content renders safely and correctly across browsers. There are 3 types of HTML entities or character reference; named entities (which begins with an ampersand and ends with a semi-colon, with some letters or a word in between. E.g; `&copy;`), decimal entities (which starts with an ampersand ‘&’, followed by pound ‘#’, and the digits that refer to the particular character of interest. E.g; `&#169;`), and hexadecimal entities (composed of the ampersand, the pound symbol, the letter x, and the ASCII code of the character of interest. E.g; `&#x00A9;`).

**The most important entities every developer should know are:**

| Character | Named Entity | Numeric | Meaning
|--|--|--|
| < | `&lt;` | `&#60;` | Less-than |
| > | `&gt;` | `&#62;` | Greater-than |
| & | `&amp;` | `&#38;` | Ampersand |
| " | `&quot;` | `&#34;` | Double quote |
| ' | `&apos;` | `&#39;` | Apostrophe |

The `pre` (preformatted) helps your text appear the way it is (the spaces, indentation, arts, and so on), it is very useful for displaying a block of code or ASCII arts and preserving user input. For example, find out how this is displayed on the browser or editor preview:

```html
<pre>
{
  "name": "Topman",
  "age": 25
}
</pre>
```

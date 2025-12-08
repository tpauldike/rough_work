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

| Character | Named Entity | Numeric | Meaning |
|--|--|--|--|
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

## Scripts in HTML
The `script` element is used to embed executable code. While you can technically write all of your JavaScript code inside the script tags, it is considered best practice to link to an external JavaScript file instead. An example is shown below:
```html
<script src="path-to-javascript-file.js"></script>
```
<u>Separation of concern</u> is a design principle where you separate your programs into distinct sections and have each section address a separate concern.
The `button` element is used to create clickable buttons on a webpage. Buttons are interactive elements that users can click to perform actions

## Understanding How `HTML` Affects SEO
```html
<meta
  name="description"
  content="Discover expert tips and techniques for gardening in small spaces, choosing the right plants, and maintaining a thriving garden."
/>
```
Although the site’s ranking on search engines is not influenced by the metadata, the meta tag allows for Search Engine Optimization by letting you provide an attractive or interesting description that appears as a preview in search results. It is a good practice to keep the description concise and precise enough. The goal is to entice users to want to click and engage. Another vital tool is the Open Graph protocol, a way of controlling how the preview appears when your web page is shared across social media platforms. When your content is shared on social media, well-crafted OG properties can enhance the appearance for your content in users' feeds. This can lead to higher click-through rates which could signal to search engines that your content is relevant and engaging. Below are examples of the use of OG in the meta tag for Search Engine Optimization:
```html
<meta content="About Topman" property="og:title" />					
<meta content="Topman Paul-Dike" property="og:site_name" />			
<meta
  property="og:decription"
  content="The exploits of a competent and experienced fullstack developer, who switched from being a Biologist"
 />	
<meta
  content="https://github.com/tpauldike/about_me/topman.png" property="og:image"										
/>													
<meta property="og:type" content="website" />		
<meta property="og:url" content="https://www.tpauldike.vercel.app" />
```
There are many more OG properties that you can set, like *description*, *audio*, *video* and *locale*. However, the open graph *url*, *image*, *type*, and *title* are the most important ones to include. Furthermore, the following can help social media render the image properly:
```html
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```
It is recommended that the image is of high quality, 1200 x 630 pixels.

## HTML Audio and Video Elements
###### Here is [my practical work](https://github.com/tpauldike/rough_work/blob/main/fullstack_course/1-html/video-and-audio.html) with HTML video and audio elements

The `audio` element supports popular audio formats like mp3, wav, and ogg. The `video` element supports mp4, ogg, and webm formats. The audio has an src attribute that has the url of the audio file, but it will not be accessible by the user (nothing will be displayed on the screen) until you add the *controls* attribute, which enables the user to control (play, pause, mute, forward, rewind, increase the playback speed, and increase the volume of) the audio. The `audio` element also has other attributes such as; *autoplay (very useful for background music), loop (to play the song repeatedly to infinity), muted (to start the song muted for the user to unmute), preload  (auto, to preload the whole thing; metadata, to preload the only duration and size; none, to preload nothing), cross origin* and more.

When it comes to audio file types, there are differences in which browsers support which type. To accommodate this, you can use source elements inside the audio element and the browser will select the first source that it understands. Here's an example of using multiple source elements for an audio element:

```html
<audio controls>							
  <source src="audio.ogg" type="audio/ogg" />		
  <source src="audio.wav" type="audio/wav" />  	
  <source src="audio.mp3" type="audio/mpeg" />	
  Your browser does not support the audio element.	
</audio>
```								
The browser will first start with the ogg type, and if it can't play the audio, then it'll move down to the next type in the list.
The video element shares the same attributes mentioned so far but has more, such as; playsinline, width, height, poster (to display an image while the video is preloading or before it plays). Below is an example:

```html
<video
src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
  loop
  controls
  muted
  poster="https://peach.blender.org/wp-content/uploads/title_anouncement.jpg?x11217"
  width="400"
></video>
```

## Common Ways to Optimize Media Assets
Size, format and compression are the 3 things to consider while using media such as images. The image shouldn’t be too large or too small; it’s unnecessary to use an image of size 1920x1080 when you want it rendered at 640x680.
There are more optimized image formats than PNG and JPG. A compression algorithm can be run to have the image (not on JPGs, to avoid reduced quality) locally compressed for optimization, so that the user doesn’t download unnecessary data while browsing your web page.

Images are considered as intellectual property and are therefore copyrighted, using them requires either obtaining written permission from the copyright holder, purchasing a license from the copyright holder, or incorporating the image in a way that falls under fair use (which is a bit dicey).
Images licensed specifically under the Creative Commons 0 license are considered public domain, they have no copyright and are free to use, such as is the case of Pixabay and Unsplash. Be mindful of the license and copyright terms before you use an image on your website. The default copyright that the creator or original owner has is the All Rights Reserved, except otherwise specified.
Copyright is the right that the owner has, while license is how much of that right he chooses to share with you.

Common image formats like PNG and JPG are classified as raster formats, because they’re pixel-based; SVG stands for a scalable vector graphic, which can be scaled to any size without impacting the quality, unlike the raster formats. Also, SVG can be coded directly in your raw HTML, using the svg element, as seen in the example below:
```html
<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="45" stroke="black" stroke-width="4" fill="yellow" />
  <circle cx="35" cy="40" r="5" fill="black" />
  <circle cx="65" cy="40" r="5" fill="black" />
  <path d="M35 65 Q50 80 65 65" stroke="black" stroke-width="4" fill="transparent" />
</svg>
```
**In the above example:**
- The `svg` element is the container for the whole drawing. It sets up the space where all the shapes appear. Everything you want to draw with SVG, such as circles, lines, or paths, goes inside the svg element.
- The `circle` element is used to make the face and the eyes. One large circle forms the yellow face, and two smaller circles make the eyes.
- The `path` element is used to draw the smile. It creates a curved line for the mouth.

Each SVG element has attributes that control its appearance and position within the drawing area
SVGs are best for icons & logos, illustrations & line arts, scalable UI graphics, animations, charts & graphs, and more. But, raster formats are better for photographs, complex (high-detail) images, and real-life scenes.

//  ******** DOM ********

// DOM it stands for Document Object Model. It is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style, and content. 
// The DOM represents the document as a tree of nodes, where each node represents an element, attribute, or piece of text in the document.    

//      window is the global object in the browser environment. It represents the browser window and provides access to various properties and methods for interacting with the browser and the document. 
//      The window object is the top-level object in the DOM hierarchy, and all other objects are properties of it.   
//      document is a property of the window object that represents the HTML document loaded in the browser. 
//      It provides access to the elements and content of the web page, allowing you to manipulate and interact with them using JavaScript.   
//      The document object is a key part of the DOM and is used to access and modify the structure, style, and content of the web page.


// <!DOCTYPE html> 
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>DOM</title>
// </head>
// <body>
//     <div class="bg-black">
//         <h1>My DOM Page</h1>
//         <p>This is a simple paragraph.</p>
//     </div>
// </body>
// </html>

// tree structure of the above HTML document:

// - Document   
//   - html
//     - head
//       - meta (charset="UTF-8")
//       - meta (name="viewport" content="width=device-width, initial-scale=1.0")
//       - title (text: "DOM")
//     - body
//       - div (class="bg-black")
//         - h1 (text: "My DOM Page")
//         - p (text: "This is a simple paragraph.")


// ************ getElementById() ************

// document.getElementById() method is a commonly used method in JavaScript that allows you to access an HTML element by its unique id attribute.
//  It takes a string argument that represents the id of the element you want to access, and it returns the first element in the document with that id. If no element with the specified id exists, it returns null. This method is useful for manipulating specific elements in the DOM based on their unique identifiers.

// For example, consider the following HTML:
// <div id="myElement">This is an element with a unique id.</div>
// If you want to access this element using JavaScript, you can use the getElementById() method like this:
// const myElement = document.getElementById('myElement');
// console.log(myElement.textContent); // Output: "This is an element with a unique id."

// ************ getElementsByClassName() ************
// get element by class name and change its backgorung colour and text

// The document.getElementsByClassName() method is a commonly used method in JavaScript that allows you to access all HTML elements that have a specific class name. It takes a string argument that represents the class name you want to access, and it returns a live HTMLCollection of all elements in the document with that class name. If no elements with the specified class name exist, it returns an empty HTMLCollection. This method is useful for manipulating multiple elements in the DOM based on their shared class name.

// For example, consider the following HTML:
// <div class="myClass">This is the first element with class "myClass".</div>
// <div class="myClass">This is the second element with class "myClass".</div>
// If you want to access all elements with the class name "myClass" and change their background color and text, you can use the getElementsByClassName() method like this:
// const elements = document.getElementsByClassName('myClass');
// for (let i = 0; i < elements.length; i++) {
//   elements[i].style.backgroundColor = 'yellow'; // Change background color to yellow
//   elements[i].textContent = 'This text has been changed.'; // Change text content
// }


//  ************ innerText, textContent, innerHTML, outerHTML ************



// difference bwtween innerText and TextContent
// innerText and textContent are both properties of DOM elements that allow you to access and manipulate the text content of an element,    
// but they have some differences in how they work:

// 1. innerText: This property returns the visible text content of an element, including any formatting and styling. 
// It takes into account CSS styles such as display: none; and visibility: hidden;, which can hide elements from being displayed on the page. 
// When you set innerText, it will update the visible text content of the element, and any HTML tags within the text will be treated as plain text.

// 2. textContent: This property returns the raw text content of an element, including all text within the element and its descendants, regardless of CSS styles.
// It does not take into account any formatting or styling, and it will include text from hidden elements. 
// When you set textContent, it will update the raw text content of the element, and any HTML tags within the text will be treated as plain text.


// for example, consider the following HTML:
// <div id="example">
//   <p>This is a <strong>paragraph</strong>.</p>
//   <p style="display: none;">This text is hidden.</p>
// </div>

// If you access the innerText and textContent properties of the div element, you will get different results:
// const exampleDiv = document.getElementById('example');
// console.log(exampleDiv.innerText); // Output: "This is a paragraph."
// console.log(exampleDiv.textContent); // Output: "This is a paragraph.This text is hidden."


// innerHTML and outerHTML are both properties of DOM elements that allow you to access and manipulate the HTML content of an element,
// but they have some differences in how they work:
// 1. innerHTML: This property returns the HTML content of an element, including all child elements and their content.
// When you set innerHTML, it will replace the existing HTML content of the element with the new HTML you provide.
// For example, if you have a div element with some content and you set its innerHTML to a new value, it will replace the existing content with the new HTML.
// 2. outerHTML: This property returns the HTML content of an element, including the element itself and all its child elements.
// When you set outerHTML, it will replace the entire element, including itself, with the new HTML you provide.
// For example, if you have a div element with some content and you set its outerHTML to a new value, it will replace the entire div element, including itself, with the new HTML.
// For example, consider the following HTML:
// <div id="example">
//   <p>This is a paragraph.</p>
// </div>
// If you access the innerHTML and outerHTML properties of the div element, you will get different results:
// const exampleDiv = document.getElementById('example');
// console.log(exampleDiv.innerHTML); // Output: "<p>This is a paragraph.</p>"
// console.log(exampleDiv.outerHTML); // Output: "<div id="example"><p>This is a paragraph.</p></div>"    



// ************ Query Selector ************

// The querySelector() method is a powerful and versatile method in JavaScript that allows you to select the first element in the DOM that matches a specified CSS selector.
// It takes a string argument that represents a CSS selector, and it returns the first element in the document that matches that selector. 
// If no elements match the selector, it returns null. The querySelector() method is commonly used to access and manipulate specific elements in the DOM based on their class, id, or other attributes.

// For example, consider the following HTML:


// <div class="container">
//   <p class="text">This is a paragraph.</p>
//   <p class="text">This is another paragraph.</p>
// </div>

// If you want to select the first paragraph element with 
// the class "text", you can use the querySelector() method like this:

// const firstParagraph = document.querySelector('.text');

// In this example, the querySelector() method will return the first paragraph element with the class "text", which is the first <p> element in the container div.


// other exxamples of seleccting elements
// selecting an element by id
// const elementById = document.querySelector('#myId');

// selecting an element by class
// const elementByClass = document.querySelector('.myClass');

// selecting an element by tag name
// const elementByTag = document.querySelector('p');



// ************** query Selector ALL ************

// here is an example






# mblog

## Introduction
This project is meant to be a new way of taking notes for math, focusing on being fast to write, but also on having organization tools built in to make the computer able to somewhat understand what you are writing about. 
It will consist of:
1) A new language for writing math notes
2) A way to turn that into a website or a LaTeX document.

The oranization tools are not just links (like the ones in Obsidian.md), but also contain metadata such as whether some block of writing is a definition, if it is a subdefinition of some other definition, etc.

This metadata can then be displayed to the user, and they can search for results, categorize definitions, and find properties of certain objects.

## Basics of the math language
There are two types of fundemental objects that you can make in the language: notes and blocks. 
### Note
A note is a file that contains information about a topic. A note could pertain to a chapter of a book, or a specific topic. A note contains writen text, similar to a markdown file, but also could contain blocks. 

### Block
A block is a way to contain a specific section of text. This is done for two reasons: to display in a box to the user, and to add metadata to categorize it. 

#### Block metadata
A block also contains the following metadata:
- A title
- A slug (i.e. a shortened version of the title that gets used for the url)
- Some preview text (i.e. what gets shown whenever there is a preview of that block, usually a summary or a statement)
- Some body text (i.e. the rest of the block)
- The type of the block (explained below)
- A list of context blocks (i.e. if the block exists in the context of some other blocks)


#### Block types
A block can be one of the following types:
- Definition: Definitions are blocks that consist of an object to be defined. An object could really be anything but usually it is some kind of structure. 

- Example: An example is an example of a definition, result or proprety. Usually it is in the context of another block, but it doesn't have to be.

- Result: A result is a lemma, theorem or corollary. It is a mathematical fact that usually will have a proof in the body section.

- Property: A property is specifically a property of an object or result. Properties of objects are generally statements that are sometimes true/false, such as commutativity. 
Properties of results are less common, but could be used as tagging results saying that a proof for a lemma was uniform, or that a certain result is a universal property, assumes the AoC, etc.

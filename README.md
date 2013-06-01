#jsonvcs

##install
`pip install jsonvcs`

##example
```python
```

##how it works
Revisions are stored in an array of reverse-diffs, which is part of a jsonvcs docment.So it provides lightweight versioning with only 1 doc being manipulated.
The current state of the doc is also stored in the document, and compiling all the diffs on to the current version (starting from the most recent), brings you back to the original doc.

Revisions are stored in the [json patch](http://tools.ietf.org/id/draft-ietf-appsawg-json-patch-02.html) format

It's also database agnostic, so you can use any way of storing your JSON, from flat files to MongoDB.

##anatomy of a version controlled doc
see the [specification](http://github.com/slang800/jsonvcs/blob/master/docs/document.schema.json), written in JSON-schema

##what it doesn't do
Jsonvcs isn't good at tracking revisions to large chunks of text. If you want to use it for this, split your text into an array of lines. It's made to track revisions to structured data, but doesn't look inside of basic datatypes like strings, or integers.

jsonvcs also doesn't provide complex operations like branching or merging. Right now, all history is "linear". If you want to do any of that fancy stuff, either roll your own VCS or store your data in flat files & use git.

##faq
**why does this use reverse diffs rather than regular ones?**

So docs can be compressed by just removing entries from the beginning of the history array.


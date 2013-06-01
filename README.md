#jsonvcs

docs can be compressed by just removing entries from the beginning of the history array

##install
`pip install jsonvcs`

##how it works
versions stored in one document... lightweight versioning w/ only 1 doc being manipulated
"reverse diffs" - the current state of the doc is readily avaliable, compiling all the diffs on to the current version (starting from the most recent), brings you back to the original doc

revisions stored in format specified by [json patch](http://tools.ietf.org/id/draft-ietf-appsawg-json-patch-02.html)

database agnostic... you can use any way of storing your JSON.

##anatomy of a version controlled doc
see the [specification](http://github.com/slang800/jsonvcs/blob/master/docs/document.schema.json), written in JSON-schema

##what it doesn't do
json-vcs isn't good at tracking revisions to large chunks of text. If you want to use it for this, split your text into an array of lines. json_vcs is made to track revisions to structured data, but doesn't look inside of basic datatypes like strings, or integers.

json_vcs also doesn't provide complex operations like branching or merging. Right now, all history is "linear". If you want to do any of that fancy stuff, either roll your own VCS or store your data in text files & use git.

##faq
**why does this use reverse diffs rather than regular ones?**

So docs can be compressed by just removing entries from the beginning of the history array.


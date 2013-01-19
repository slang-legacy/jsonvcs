#jsonvcs

docs can be compressed by just removing entries from the beginning of the history array

making a revision:
 - get doc from db
 - determine what needs to be changed in the new doc to get back to the old doc... save that as a diff (append obj to diff array along with diff metadata)
 - replace the old doc w/ the new one
 - save to db

maybe add caching for docs so old versions of the doc can be stored w/out needing to be calculated... not really needed yet since revisions would be minimal on the CSD

##how it works
versions stored in one document... lightweight versioning w/ only 1 doc being manipulated
"reverse diffs" - the current state of the doc is readily avaliable, compiling all the diffs on to the current version (starting from the most recent), brings you back to the original doc

revisions stored in format specified by json patch http://tools.ietf.org/id/draft-ietf-appsawg-json-patch-02.html

database agnostic... you can use any way of storing your JSON.

##anatomy of a version controlled doc
see the [specification](./json-vcs/blob/master/docs/document.schema.json), written in JSON-schema

##what it doesn't do
json-vcs isn't good at tracking revisions to large chunks of text. If you want to use it for this, split your text into an array of lines. json_vcs is made to track revisions to structured data, but doesn't look inside of basic datatypes like strings, or integers.

json_vcs also doesn't provide complex operations like branching or merging. Right now, all history is "linear". If you want to do any of that fancy stuff, either roll your own VCS or store your data in text files & use git.
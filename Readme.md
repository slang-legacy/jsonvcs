mongodb versioning for python
versions stored in one document... lightweight versioning w/ only 1 doc being manipulated
"reverse diffs" - the current state of the doc is readily avaliable, compiling all the diffs on to the current version (starting from the most recent), brings you back to the origional doc
deal with all the stuff using a class for saving n' stuff... maybe extend the class provided by pymongo
docs can be compressed by just cutting the diffs array down

making a revision:
 - get doc from db
 - determine what needs to be changed in the new doc to get back to the old doc... save that as a diff (append obj to diff array along with diff metadata)
 - replace the old doc w/ the new one
 - save to db

class just needs to provide save method & way to get a list of all the diffs
and support metadata
provide method to calculate doc at specific point... needs to start w/ current obj and work backwards... maybe let the obj nearist in time, be passed to that function to shortcut the calculation process
maybe add caching for docs so old versions of the doc can be stored w/out needing to be calculated... not really needed yet since revisions would be minimal on the CSD
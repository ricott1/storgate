function onCreated(tab) {
  console.log(`Created new tab: ${tab.id}`)
}

function onError(error) {
  console.log(`Error: ${error}`);
}

browser.browserAction.onClicked.addListener(function() {
  var creating = browser.tabs.create({
    url:"http://tnsksqdywtzhe5yrel5b5apizwhfbiqrhhmjmg66vtojkdmiascrlpyd.onion"
  });
  creating.then(onCreated, onError);
});
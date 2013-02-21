backwindow=chrome.extension.getViews();
popdiv=document.getElementById('pop')
popdiv.innerHTML='<b>im pop</b>'

chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.executeScript(null,
                           {code:"document.body.bgColor='red'"});
});

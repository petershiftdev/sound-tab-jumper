let cycleTabIds = [];
let cycleIndex = -1;
let originTabId = null;

function resetCycle() {
  cycleTabIds = [];
  cycleIndex = -1;
  originTabId = null;
}

async function startCycle(originTab) {
  resetCycle();

  if (!originTab?.id) {
    return;
  }

  const tabs = await chrome.tabs.query({});
  const soundTabIds = tabs
    .filter(tab => tab.audible && tab.id !== originTab.id)
    .map(tab => tab.id);

  if (soundTabIds.length === 0) {
    return;
  }

  originTabId = originTab.id;
  cycleTabIds = [...soundTabIds, originTabId];
  cycleIndex = -1;
}

async function getExistingTabIds() {
  const tabs = await chrome.tabs.query({});
  return new Set(tabs.map(tab => tab.id));
}

async function tryActivateTab(tabId) {
  try {
    const tab = await chrome.tabs.get(tabId);
    await chrome.windows.update(tab.windowId, { focused: true });
    await chrome.tabs.update(tab.id, { active: true });
    return true;
  } catch {
    return false;
  }
}

async function jumpToNextSoundTab(currentTab) {
  for (let attempt = 0; attempt < 2; attempt++) {
    if (cycleTabIds.length === 0) {
      await startCycle(currentTab);
      if (cycleTabIds.length === 0) {
        return;
      }
    }

    const existing = await getExistingTabIds();
    const cycleLength = cycleTabIds.length;

    for (let step = 0; step < cycleLength; step++) {
      cycleIndex = (cycleIndex + 1) % cycleLength;
      const tabId = cycleTabIds[cycleIndex];

      if (!existing.has(tabId)) {
        continue;
      }

      const activated = await tryActivateTab(tabId);
      if (!activated) {
        continue;
      }

      if (tabId === originTabId) {
        resetCycle();
      }

      return;
    }

    resetCycle();
  }
}

chrome.action.onClicked.addListener(jumpToNextSoundTab);

chrome.commands.onCommand.addListener(async command => {
  if (command !== "jump-to-sound-tab") {
    return;
  }

  const [tab] = await chrome.tabs.query({
    active: true,
    lastFocusedWindow: true
  });
  await jumpToNextSoundTab(tab);
});

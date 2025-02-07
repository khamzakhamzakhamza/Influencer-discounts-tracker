export default function RunningInBrowser() : boolean {
  return !chrome.runtime?.id;
}
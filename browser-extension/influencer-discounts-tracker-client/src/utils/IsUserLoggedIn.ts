// import { User } from "../entities/User";

export default function IsUserLoggedIn(setFunc: (v: boolean) => void) : void {
  setFunc(false);
  /* TODO: Set up properly later
  chrome.storage.local.get('user', (result: any) => {
    console.log(result);
    if (result.user) {
      setFunc(true);
    } else {
      setFunc(false);
    }
  }); */
}

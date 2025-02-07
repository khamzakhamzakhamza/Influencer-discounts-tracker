import { User } from "../entities/User";
import RunningInBrowser from "../utils/RunningInBrowser";

export const LoginUser = async (username: string): Promise<User> => {
  var id = crypto.randomUUID()
  var user : User = {id, username};
  
  // TODO: make an api call to register user 
  
  if (RunningInBrowser())
    localStorage.setItem('user', JSON.stringify(user));
  else 
    chrome.storage.local.set({'user': user});

  return user;
}

export const GetCurrentUser = (setFunc: (u: User | null) => void): void => RunningInBrowser()
  ? setFunc(JSON.parse(localStorage.getItem('user') || 'null'))
  : chrome.storage.local.get('user', (result: any) => setFunc(result.user));

export const LogoutUser = (): Promise<void> => RunningInBrowser() 
  ? new Promise(() => localStorage.removeItem('user'))
  : chrome.storage.local.remove('user');

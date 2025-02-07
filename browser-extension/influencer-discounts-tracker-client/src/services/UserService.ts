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

export const GetCurrentUser = () : User | null => {
  let user : User | null = null;

  if (RunningInBrowser())
    user = JSON.parse(localStorage.getItem('user') || 'null');
  else
    chrome.storage.local.get('user', (result: any) => {
    console.log(result);
    user = result.user;
  });
  
  return user;
}

export const LogoutUser = (): void => {
  if (RunningInBrowser())
    localStorage.removeItem('user');
  else
    chrome.storage.local.remove('user');
}

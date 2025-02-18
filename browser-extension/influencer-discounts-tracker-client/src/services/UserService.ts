import { API_HOST } from "../AppConfig";
import { User } from "../entities/User";
import RunningInBrowser from "../utils/RunningInBrowser";

export const LoginUser = async (username: string): Promise<User> => {
  const response = await fetch(`${API_HOST}/api/v1/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username })
  });

  const responseData = await response.json();
  const user = responseData;

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

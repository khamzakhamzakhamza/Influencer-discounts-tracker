import { createContext, useEffect, useState } from "react";
import { User } from "../entities/User";
import { GetCurrentUser } from "../services/UserService";

export const UserContext = createContext<any>(null);

type Props = {
  children?: React.ReactNode
};

const UserProvider: React.FC<Props> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const handleStorageChange = () => setUser(GetCurrentUser());
    handleStorageChange();

    window.addEventListener("storage", handleStorageChange);
    return () => window.removeEventListener("storage", handleStorageChange);
  }, []);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
};

export default UserProvider;
import { Button, Flex, Typography } from 'antd';
import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext';
import { User } from '../entities/User';
import { LogoutUser } from '../services/UserService';

const { Text } = Typography;

const UserInfoRow: React.FC = () => {
  const userContext = useContext(UserContext);
  const user = userContext?.user as User;

  const lougoutClick = () => {
    LogoutUser();
    userContext?.setUser(null);
  }

  return (
    <Flex 
      align='center'
      justify='space-between'
      gap={10}
    >
      <Text>Welcome <b>{user.username}</b>!</Text>
      <Button type='text' onClick={lougoutClick}>Logout</Button>
    </Flex>
  )
};

export default UserInfoRow;

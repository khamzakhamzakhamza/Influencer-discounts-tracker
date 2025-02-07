import { Space, Typography } from 'antd';
import React from 'react';
import LoginForm from '../components/LoginForm';

const { Title } = Typography;

const LoginScreen: React.FC = () => (
  <Space 
    direction='vertical'
    style={{width: '100%'}}
  >
    <Title 
      level={4}
      style={{marginTop: '10px'}}
    >
      Login
    </Title>
    <LoginForm/>
  </Space>
);

export default LoginScreen;

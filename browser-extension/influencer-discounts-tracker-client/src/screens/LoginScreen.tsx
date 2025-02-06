import { Space, Typography } from 'antd';
import React from 'react';
import LoginForm from '../components/LoginForm';

const { Title } = Typography;

const LoginScreen: React.FC = () => (
  <Space direction='vertical'>
    <Title level={4}>Login</Title>
    <LoginForm/>
  </Space>
);

export default LoginScreen;

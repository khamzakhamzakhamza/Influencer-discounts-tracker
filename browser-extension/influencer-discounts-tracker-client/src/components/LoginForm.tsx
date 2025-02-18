import { Button, Form, FormProps, Input } from 'antd';
import React, { useContext, useState } from 'react';
import { LoginUser } from '../services/UserService';
import { UserContext } from '../context/UserContext';

type LoginFormProps = {
  username: string;
}

const LoginForm: React.FC = () => {
  const userContext = useContext(UserContext);
  const [loading, setLoading] = useState(false);

  const onFinish: FormProps<LoginFormProps>['onFinish'] = async (values: LoginFormProps) => {
    setLoading(true);
    const user = await LoginUser(values.username);
    setLoading(false);
    userContext?.setUser(user);
  };

  return (
    <Form
      name="login"
      initialValues={{ remember: true }}
      onFinish={onFinish}
    >
      <Form.Item
        label="Username"
        name="username"
        rules={[{ required: true, message: 'Please input your username' }]}
      >
        <Input />
      </Form.Item>
      <Form.Item>
        <Button block type="primary" htmlType="submit" loading={loading}>
          Login
        </Button>
      </Form.Item>
    </Form>
  )
};

export default LoginForm;

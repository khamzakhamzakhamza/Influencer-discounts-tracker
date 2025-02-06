import { Button, Form, FormProps, Input } from 'antd';
import React from 'react';

type LoginFormProps = {
  username: string;
}

const onFinish: FormProps<LoginFormProps>['onFinish'] = (values) => {
  console.log('Success:', values);
};

const LoginForm: React.FC = () => (
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
      <Button type="primary" htmlType="submit">
        Login
      </Button>
    </Form.Item>

  </Form>
);

export default LoginForm;

import { Space, Typography } from 'antd';
import React from 'react';
import UserInfoRow from '../components/UserInfoRow';

const { Title } = Typography;

const WatchlistScreen: React.FC = () => (
  <Space 
    direction='vertical'
    style={{ width: '100%' }}
  >
    <Title 
      level={4}
      style={{marginTop: '10px'}}
    >
      Your watchlist
    </Title>
    <UserInfoRow />
  </Space>
);

export default WatchlistScreen;

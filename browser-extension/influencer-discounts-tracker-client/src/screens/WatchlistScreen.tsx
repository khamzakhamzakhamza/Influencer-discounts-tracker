import { Space, Typography } from 'antd';
import React from 'react';

const { Title } = Typography;

const WatchlistScreen: React.FC = () => (
  <Space direction='vertical'>
    <Title level={4}>Your watchlist</Title>
  </Space>
);

export default WatchlistScreen;

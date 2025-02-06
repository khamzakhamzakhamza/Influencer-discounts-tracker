import { ConfigProvider, Layout, theme, Typography } from 'antd';
import React, { useEffect, useState } from 'react';
import WatchlistScreen from './screens/WatchlistScreen';
import IsUserLoggedIn from './utils/IsUserLoggedIn';
import LoginScreen from './screens/LoginScreen';

const { Header, Content } = Layout;
const { Title } = Typography;

const App: React.FC = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => IsUserLoggedIn(setIsLoggedIn), []);
  
  return (
    <ConfigProvider
      theme={{
        components: {
          Form: {
            padding: 10
          }
        },
        token: {colorPrimary: "890ccc"},
        algorithm: [theme.darkAlgorithm, theme.compactAlgorithm]
      }}
    > 
      <Layout style={{height: '100%'}}>
        <Header style={{padding: '0px 10px'}}>
          <Title level={4}>Influencer Discounts Tracker</Title>
        </Header>
        <Content style={{padding: '10px'}}>
          {isLoggedIn ? <WatchlistScreen/> : <LoginScreen/>}
        </Content>
      </Layout>
    </ConfigProvider>
  );
};

export default App;

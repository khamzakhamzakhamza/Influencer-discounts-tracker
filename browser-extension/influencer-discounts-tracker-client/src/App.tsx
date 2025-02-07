import { ConfigProvider, Layout, theme, Typography } from 'antd';
import React, { useContext } from 'react';
import WatchlistScreen from './screens/WatchlistScreen';
import LoginScreen from './screens/LoginScreen';
import { UserContext } from './context/UserContext';

const { Header, Content } = Layout;
const { Title } = Typography;

const App: React.FC = () => {
  const userContext = useContext(UserContext);

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
        <Header style={{padding: '0px 15px'}}>
          <Title level={4}>Influencer Discounts Tracker</Title>
        </Header>
        <Content style={{padding: '15px'}}>
          {userContext?.user ? <WatchlistScreen/> : <LoginScreen/>}
        </Content>
      </Layout>
    </ConfigProvider>
  );
};

export default App;

import { useCallback, useContext, useEffect, useState } from "react";
import { DeleteInfluencer, GetInfluencers } from "../services/InfluencerService";
import { Influencer } from "../entities/Influencer";
import { User } from "../entities/User";
import { UserContext } from "../context/UserContext";
import { List, Skeleton } from "antd";
import InfluencerInfoRow from "./InfluencerInfoRow";
import InfiniteScroll from "react-infinite-scroll-component";

const Watchlist: React.FC = () => {
  const userContext = useContext(UserContext);
  const user = userContext?.user as User;

  const [loading, setLoading] = useState(false);
  const [data, setData] = useState<Influencer[]>([]);

  const loadMoreData = useCallback(async () => {
    if (loading) return;

    setLoading(true);
    const influencers = await GetInfluencers(user.username);
    setData(influencers);
    setLoading(false);
  }, [loading, user.username]);

  useEffect(() => {loadMoreData()}, [loadMoreData]);

  const deleteInfluencer = async (influencer: Influencer) => {
    await DeleteInfluencer(user.username, influencer);
    await loadMoreData();
  };
  
  return (
    <div
      id="scrollableDiv"
      style={{
        height: 390,
        overflow: 'auto',
      }}
    >
      <InfiniteScroll
        dataLength={data.length}
        next={loadMoreData}
        hasMore={data.length < 1}
        loader={<Skeleton avatar paragraph={{ rows: 1 }} active />}
        scrollableTarget="scrollableDiv"
      >
        <List>{data.map((influencer) => <InfluencerInfoRow influencer={influencer} deleteInfluencer={deleteInfluencer}/>)}</List>
      </InfiniteScroll>
    </div>
  );
};

export default Watchlist;

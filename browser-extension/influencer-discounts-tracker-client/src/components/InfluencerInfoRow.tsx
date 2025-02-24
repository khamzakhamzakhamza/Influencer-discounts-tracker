import { Influencer } from "../entities/Influencer";
import { Avatar, Button, List } from "antd";
import { DeleteOutlined } from '@ant-design/icons';
import { useContext } from "react";
import { UserContext } from "../context/UserContext";
import { User } from "../entities/User";
import { DeleteInfluencer } from "../services/InfluencerService";

type InfluencerInfoRowProps = {
  influencer: Influencer;
  refetchData: () => void;
}

const InfluencerInfoRow: React.FC<InfluencerInfoRowProps> = (props: InfluencerInfoRowProps) => {
  const userContext = useContext(UserContext);
  const user = userContext?.user as User;
  const { influencer, refetchData } = props;

  const deleteInfluencer = async () => {
    await DeleteInfluencer(user.username, influencer);
    refetchData();
  };

  return (
    <List.Item>
      <List.Item.Meta
        avatar={<Avatar src={influencer.imageUrl} />}
        title={influencer.title}
        description={<a href={influencer.channelUrl} target="_blank">{influencer.username}</a>}
      />
      <Button 
        type='text' 
        onClick={deleteInfluencer}
      >
        <DeleteOutlined />
      </Button>
    </List.Item>
  );
};

export default InfluencerInfoRow;

import { Influencer } from "../entities/Influencer";
import { Avatar, Button, List } from "antd";
import { DeleteOutlined } from '@ant-design/icons';

type InfluencerInfoRowProps = {
  influencer: Influencer;
  deleteInfluencer: (influencer: Influencer) => void;
}

const InfluencerInfoRow: React.FC<InfluencerInfoRowProps> = (props: InfluencerInfoRowProps) => {
  const { influencer, deleteInfluencer } = props;

  return (
    <List.Item>
      <List.Item.Meta
        avatar={<Avatar src={influencer.imageUrl} />}
        title={influencer.title}
        description={<a href={influencer.channelUrl} target="_blank" rel="noreferrer">{influencer.username}</a>}
      />
      <Button 
        type='text' 
        onClick={() => deleteInfluencer(influencer)}
      >
        <DeleteOutlined />
      </Button>
    </List.Item>
  );
};

export default InfluencerInfoRow;

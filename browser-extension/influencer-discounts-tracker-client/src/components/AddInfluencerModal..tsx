import { Button, Input, Modal, Typography } from "antd";
import { useContext, useState } from "react";
import { AddInfluencer } from "../services/InfluencerService";
import { UserContext } from "../context/UserContext";
import { User } from "../entities/User";
import { Influencer } from "../entities/Influencer";

type InfluencerInfoRowProps = {
  influencerAdded: (influencer: Influencer) => Promise<void>;
}

const AddInfluencerModal: React.FC<InfluencerInfoRowProps> = (props: InfluencerInfoRowProps) => {
  const userContext = useContext(UserContext);
  const user = userContext?.user as User;

  const { influencerAdded } = props;

  const { Text } = Typography;
  
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<string>('');
  const [resultColor, setResultColor] = useState<"success" | "danger">('success');
  const [link, setLink] = useState<string>('');

  const handleOk = async () => {
    setLoading(true);

    try {
      const influencer = await AddInfluencer(user.username, link);
      await influencerAdded(influencer);
      setResultColor('success');
      setResult(`Successfully added ${influencer.username} to watchlist`);
      setLink('');
    }
    catch (e: any) {
      setResultColor('danger');
      setResult(`Failed to add influencer to watchlist: ${e.message}`);
    }
    finally {
      setLoading(false);
    }
  };

  const handleCancel = () => {
    setOpen(false);
    setResult('');
  }

  return (
    <>
      <Button type="primary" block onClick={() => setOpen(true)}>
        Add Influencer to my Watchlist
      </Button>
      <Modal
        title="Add Influencer to Watchlist"
        open={open}
        confirmLoading={loading}
        onCancel={handleCancel}
        footer={[
          <Button key="submit" type="primary" loading={loading} onClick={handleOk}>
            Submit
          </Button>
        ]}
      >
        <Text type={resultColor}>{result}</Text>
        <Input placeholder="Youtube channel link"
          value={link}
          onChange={(e) => setLink(e.target.value)}/>
      </Modal>
    </>
  );
};

export default AddInfluencerModal;

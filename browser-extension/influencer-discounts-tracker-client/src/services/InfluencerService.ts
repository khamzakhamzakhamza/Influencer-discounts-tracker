import { API_HOST } from "../AppConfig";
import { Influencer } from "../entities/Influencer";

export const GetInfluencers = async (username: string): Promise<Influencer[]> => {
  const response = await fetch(`${API_HOST}/api/v1/influencers?username=${username}`);
  return await response.json();
}

export const AddInfluencer = async (username: string, link: string): Promise<Influencer> => {
  const response = await fetch(`${API_HOST}/api/v1/influencers`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, link })
  });

  const responseData = await response.json();
  return responseData;
}

export const DeleteInfluencer = async (username: string, influencer: Influencer): Promise<void> => {
  await fetch(`${API_HOST}/api/v1/influencers?username=${username}&influencer_id=${influencer.id}`, {
    method: 'DELETE'
  });
}

import { API_HOST } from "../AppConfig";
import { Influencer } from "../entities/Influencer";

export const GetInfluencers = async (username: string): Promise<Influencer[]> => {
  const influencers = [
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'},
    {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'}
  ];

  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(influencers);
    }, 2000);
  });
  // const response = await fetch(`${API_HOST}/api/v1/influencers/${username}`);
  // return await response.json();
}

export const AddInfluencer = async (username: string, link: string): Promise<Influencer> => {
  const influencer = {id: '1', username: '@WeeklyPlanetPodcast', title: 'The Weekly Planet', channelUrl: 'https://www.youtube.com/@WeeklyPlanetPodcast', imageUrl: 'https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj'};

  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(influencer);
    }, 2000);
  });
}

export const DeleteInfluencer = async (username: string, influencer: Influencer): Promise<void> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve();
    }, 2000);
  });
}

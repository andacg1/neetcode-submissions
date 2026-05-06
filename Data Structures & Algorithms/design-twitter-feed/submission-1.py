from heapq import *
class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.tweet_index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.tweet_index, tweetId))
        self.tweet_index += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followed_users = self.following[userId]
        def get_tweets(user_id: int):
            nonlocal heap
            tweets = self.user_tweets[user_id]
            for tweetId in tweets:
                heappush(heap, tweetId)
                while len(heap) > 10:
                    heappop(heap)
        get_tweets(userId)
        for other_user in list(followed_users):
            get_tweets(other_user)
        return list(map(lambda item: item[1], sorted(heap, reverse=True)))

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
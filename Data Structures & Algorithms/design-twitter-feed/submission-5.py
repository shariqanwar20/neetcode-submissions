class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((tweetId, self.time * -1))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]: # 2
        # 1: [(abc, -1), (def, -4), (ghi, -6)]
        # 2: [(jk, -2), (lm, -5), (no, -7)]
        # 
        #
        #
        #
        self.follow_map[userId].add(userId)
        # push user and those he follows last tweet (1, -6) in heap
        # pop from the heap and push the tweet which was popped earlier tweet
        # repeat until we have 10 tweets at max or no more tweets to process
        recent = []
        print(self.tweet_map)
        for person in self.follow_map[userId]:
            size = len(self.tweet_map[person]) - 1
            if size >= 0:
                heapq.heappush(recent, (self.tweet_map[person][size][1], person, size))
        
        # print(recent)
        res = []
        while recent and len(res) < 10:
            _, user, idx = heapq.heappop(recent)
            res.append(self.tweet_map[user][idx][0])

            idx -= 1
            if (idx) >= 0:
                heapq.heappush(recent, (self.tweet_map[user][idx][1], user, idx))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        # person -> those who this person follows
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

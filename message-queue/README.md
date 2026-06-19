# Design Message Queue

## Requirements
- The queue should be in-memory and should not require access to the file system.
- There can be multiple topics in the queue.
- A (string) message can be published on a topic by a producer/publisher and consumers/subscribers can subscribe to the topic to receive the messages.
- There can be multiple producers and consumers.
- A producer can publish to multiple topics.
- A consumer can listen to multiple topics.

### Future extension
- Support async delivery
- Support DLQ
- Support multithreading

## Design
### Entiries
- Queue
- Topic
- Publisher
- Subscriber

**Subscriber**
- name
- notify(): Boolean

**Topic**
- name
- subscribers: List[Subscriber]
- addSubscriber(): None

**Queue**
- name
- topics: Dict[str, Topic]

**Publisher**
- publish(): None

**Message**
- queue: str
- topic: str
- body: Any

**MessageQueueSystem**
- queues: Dict[str, Queue]
- createQueue(): Queue
- createTopic(): Topic
- createSubscriber(): Subscriber
- addSubscriber(): None
- createPublisher(): Publisher
- publishMessage(): None

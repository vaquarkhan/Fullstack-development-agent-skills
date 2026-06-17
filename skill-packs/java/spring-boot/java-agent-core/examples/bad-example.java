// BAD — unbounded loop, repository called directly from agent, no auth on tools
while (true) {
    var reply = chatClient.prompt().user(input).call().content();
    orderRepository.save(parse(reply)); // no tool boundary
}

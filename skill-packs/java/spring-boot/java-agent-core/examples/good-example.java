// GOOD — bounded agent loop with tool registry and max iterations
@Service
@RequiredArgsConstructor
public class SupportAgentService {
    private final ChatClient chatClient;
    private static final int MAX_STEPS = 8;

    public AgentResult run(AgentRequest request) {
        for (int step = 0; step < MAX_STEPS; step++) {
            AgentStep result = chatClient.prompt()
                .user(request.prompt())
                .call()
                .entity(AgentStep.class);
            if (result.isTerminal()) {
                return AgentResult.done(result);
            }
        }
        throw new AgentBudgetExceededException(MAX_STEPS);
    }
}

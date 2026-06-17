// GOOD — streamText with tools, onFinish logging, abort signal
const result = streamText({
  model: openai('gpt-4o'),
  system: systemPrompt,
  messages,
  tools: { lookupOrder: orderTool },
  maxSteps: 5,
  abortSignal: req.signal,
  onFinish: ({ usage, finishReason }) => audit.log({ usage, finishReason }),
});
return result.toDataStreamResponse();

class ApiClient {
  ApiClient({required this.baseUrl, required this.tokenProvider});
  final String baseUrl;
  final Future<String?> Function() tokenProvider;

  Future<ApiResponse> get(String path) async { /* dio/http with auth header */ }
}

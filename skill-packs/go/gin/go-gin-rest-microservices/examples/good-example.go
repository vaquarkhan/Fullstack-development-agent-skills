// GOOD — thin handler, context passed, typed response
func (h *OrderHandler) Create(c *gin.Context) {
    var req CreateOrderRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        c.JSON(http.StatusBadRequest, problem(err))
        return
    }
    resp, err := h.service.Create(c.Request.Context(), req)
    if err != nil {
        c.JSON(http.StatusInternalServerError, problem(err))
        return
    }
    c.JSON(http.StatusCreated, resp)
}

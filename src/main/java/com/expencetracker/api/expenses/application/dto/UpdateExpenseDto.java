package com.expencetracker.api.expenses.application.dto;

import com.expencetracker.api.expenses.domain.model.Category;
import jakarta.validation.constraints.NotNull;

public record UpdateExpenseDto(

        @NotNull
        Long expenses_ids,

        String names,
        String descriptions,
        Double amounts,
        Category categories) {
}

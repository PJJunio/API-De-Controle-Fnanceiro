package com.expencetracker.api.expenses.application.dto;

import com.expencetracker.api.expenses.domain.model.Category;
import org.antlr.v4.runtime.misc.NotNull;

public record ExpensesDto(

        @NotNull
        String names,

        String descriptions,

        @NotNull
        Double amounts,

        @NotNull
        Category categories,

        @NotNull
        Long users_ids) {
}

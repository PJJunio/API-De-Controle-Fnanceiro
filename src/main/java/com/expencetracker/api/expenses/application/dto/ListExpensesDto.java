package com.expencetracker.api.expenses.application.dto;

import com.expencetracker.api.expenses.domain.model.Category;
import com.expencetracker.api.expenses.domain.model.Expenses;

public record ListExpensesDto(Long expenses_ids, String names, String descriptions, Double amounts, Category category) {

    public ListExpensesDto (Expenses expenses){
        this(expenses.getExpenses_ids(), expenses.getNames(), expenses.getDescriptions(), expenses.getAmounts(), expenses.getCategories());
    }
}

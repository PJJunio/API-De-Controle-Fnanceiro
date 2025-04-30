package com.expencetracker.api.expenses.domain.model;


import com.expencetracker.api.auth.domain.model.User;
import com.expencetracker.api.expenses.application.dto.ExpensesDto;
import com.expencetracker.api.expenses.application.dto.UpdateExpenseDto;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "expenses")
public class Expenses {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long expenses_ids;

    private String names;
    private String descriptions;
    private Double amounts;

    @Enumerated(EnumType.STRING)
    private Category categories;

    private Boolean active = true;

    @ManyToOne @JoinColumn(name = "users_ids")
    private User user;

    public Expenses(ExpensesDto expensesDto) {
        this.names = expensesDto.names();
        this.descriptions = expensesDto.descriptions();
        this.amounts = expensesDto.amounts();
        this.categories = expensesDto.categories();
    }

    public void updateExpense(UpdateExpenseDto updateExpenseDto) {
        if (updateExpenseDto.names() != null) {
            this.names = updateExpenseDto.names();
        }
        if (updateExpenseDto.descriptions() != null) {
            this.descriptions = updateExpenseDto.descriptions();
        }
        if (updateExpenseDto.amounts() != null) {
            this.amounts = updateExpenseDto.amounts();
        }
        if (updateExpenseDto.categories() != null) {
            this.categories = updateExpenseDto.categories();
        }
    }
}

package com.expencetracker.api.expenses.presentation.rest;

import com.expencetracker.api.auth.domain.repositories.UserRepository;
import com.expencetracker.api.expenses.application.dto.ExpensesDto;
import com.expencetracker.api.expenses.application.dto.ListExpensesDto;
import com.expencetracker.api.expenses.application.dto.UpdateExpenseDto;
import com.expencetracker.api.expenses.domain.model.Expenses;
import com.expencetracker.api.expenses.domain.repositories.ExpensesRepository;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/expenses")
public class ExpensesController {

    @Autowired
    private ExpensesRepository expensesRepository;
    @Autowired
    private UserRepository userRepository;

    @PostMapping
    @Transactional
    public void cadastraExpense(@RequestBody ExpensesDto expensesDto) {
        var expenses = new Expenses(expensesDto);
        userRepository.findById(expensesDto.users_ids())
                .ifPresent(expenses::setUser);
        expensesRepository.save(expenses);
    }

    @GetMapping("/list/user/{userId}")
    @Transactional
    public Page<ListExpensesDto> listarDespesasPorUsuario(
            @PathVariable Long userId,
            @PageableDefault(size = 10, sort = {"names"}) Pageable paginacao) {
        return expensesRepository.findByUserId(userId, paginacao).map(ListExpensesDto::new);
    }

    @PutMapping("/update/{id}")
    @Transactional
    public void atualizarDespesas(@PathVariable Long id, @RequestBody @Valid UpdateExpenseDto updateExpenseDto) {
        var expense = expensesRepository.getReferenceById(id);
        expense.updateExpense(updateExpenseDto);
    }

    @DeleteMapping("/delete/users/{userId}/expenses/{id}")
    @Transactional
    public void deletarDespesaDoUsuario(@PathVariable Long userId, @PathVariable Long id) {
        expensesRepository.deleteById(id);
    }
}

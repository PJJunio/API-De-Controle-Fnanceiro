package com.expencetracker.api.expenses.domain.repositories;

import com.expencetracker.api.expenses.domain.model.Expenses;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ExpensesRepository extends JpaRepository<Expenses, Long> {
    Page<Expenses> findByUserId(Long id, Pageable pageable);


}

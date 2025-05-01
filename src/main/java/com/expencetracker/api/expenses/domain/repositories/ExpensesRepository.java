package com.expencetracker.api.expenses.domain.repositories;

import com.expencetracker.api.expenses.domain.model.Expenses;
import jakarta.transaction.Transactional;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.UUID;

public interface ExpensesRepository extends JpaRepository<Expenses, Long> {
    @Query("SELECT e FROM Expenses e WHERE e.user.externalId = :userId")
    Page<Expenses> findByUserExternalId(@Param("userId") UUID userId, Pageable pageable);
    Expenses getReferenceById(Long id);

    @Transactional
    @Modifying
    @Query("DELETE FROM Expenses e WHERE e.id = :id AND e.user.externalId = :userId")
    int deleteByIdAndUserId(@Param("id") Long id, @Param("userId") UUID userId);

}


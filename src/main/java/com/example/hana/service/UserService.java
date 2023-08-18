package com.example.hana.service;

import com.example.hana.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

;

@Service
@RequiredArgsConstructor
public class UserService {
    private final UserRepository userRepository;
}
